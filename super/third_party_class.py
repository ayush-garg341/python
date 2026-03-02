# ─────────────────────────────────────────────────────────────────────────────
#  PART 3 — THIRD-PARTY (NON-COOPERATIVE) CLASSES
# ─────────────────────────────────────────────────────────────────────────────
#
# The realistic problem: you want to use a class from a library that was
# NOT designed for cooperative inheritance. It doesn't use super().
# Its __init__ has a rigid positional signature.
# You can't modify it.
#
# You have three options:
#   3a. Use it directly (the naive approach) — breaks other classes
#   3b. Inherit from it (also breaks things)
#   3c. WRAP it with an Adapter (the correct solution)
#
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("PART 3 — THIRD-PARTY (NON-COOPERATIVE) CLASSES")
print("=" * 70)

# This simulates a third-party class you cannot modify:
# - Has a positional-only __init__ signature
# - Does not call super()
# - Does not inherit from your Root class


class ThirdPartyDatabase:
    """Imagine this is from a library you installed via pip."""

    def __init__(self, host, port):  # rigid positional signature
        self.host = host
        self.port = port
        print(f"  ThirdPartyDatabase.__init__: connecting to {host}:{port}")
        # NO super() call — this was never designed for cooperative inheritance

    def query(self):
        print(f"  ThirdPartyDatabase.query: running on {self.host}:{self.port}")

    def close(self):
        print(f"  ThirdPartyDatabase.close: closing {self.host}:{self.port}")


print("\n[3 Setup] ThirdPartyDatabase — cannot be modified, no super():")
db = ThirdPartyDatabase("localhost", 5432)
db.query()

# ── 3a. NAIVE DIRECT INHERITANCE — BREAKS ───────────────────────────────────
#
# "I'll just inherit from it like normal."
# Problem: ThirdPartyDatabase.__init__ has a rigid (host, port) signature
# with no **kwargs. It will CRASH if anything tries to pass extra args,
# and it won't forward the chain to other cooperative classes.

print("\n" + "-" * 50)
print("[3a] Naive inheritance — why it breaks:\n")

# The problem: ThirdPartyDatabase.__init__(host, port) has NO **kwargs.
# If a cooperative mixin calls super().__init__(**kwargs), and
# ThirdPartyDatabase is next in the MRO, it crashes because it
# doesn't know what to do with those extra keyword args.


class LoggingMixin:
    def __init__(self, **kwargs):
        print(f"  LoggingMixin.__init__ running")
        self.log = []
        super().__init__(**kwargs)  # tries to pass kwargs down the chain

    def query(self):
        self.log.append("query")
        print(f"  LoggingMixin.query: logging call")
        super().query()


class CachingMixin:
    def __init__(self, **kwargs):
        print(f"  CachingMixin.__init__ running")
        self.cache = {}
        super().__init__(**kwargs)

    def query(self):
        print(f"  CachingMixin.query: checking cache")
        super().query()


# Attempt 1: use super() directly with ThirdPartyDatabase in the hierarchy
class LoggedDB_attempt1(LoggingMixin, ThirdPartyDatabase):
    def __init__(self, host, port):
        print(f"  LoggedDB_attempt1.__init__")
        super().__init__(host=host, port=port)  # passes as kwargs


print("MRO of LoggedDB_attempt1:", [c.__name__ for c in LoggedDB_attempt1.__mro__])
print("\nLoggedDB_attempt1('db.example.com', 5432) — will CRASH:\n")
try:
    naive_db = LoggedDB_attempt1("db.example.com", 5432)
except TypeError as e:
    print(f"  *** TypeError: {e}")
    print("  *** ThirdPartyDatabase.__init__ doesn't accept **kwargs!")

# Attempt 2: use direct calls to work around it
print("\nAttempt 2: use direct calls to avoid the crash:\n")


class LoggedDB_attempt2(LoggingMixin, ThirdPartyDatabase):
    def __init__(self, host, port):
        print(f"  LoggedDB_attempt2.__init__")
        self.log = []  # manually init LoggingMixin state
        ThirdPartyDatabase.__init__(
            self, host, port
        )  # direct call to ThirdPartyDatabase


print("MRO:", [c.__name__ for c in LoggedDB_attempt2.__mro__])
print()
db2 = LoggedDB_attempt2("db.example.com", 5432)
db2.query()
print(f"\n  This 'works'... but breaks as soon as you add more mixins.\n")

# Attempt 3: add CachingMixin too — double-init problem appears
print("Attempt 3: add CachingMixin — double __init__ problem:\n")

init_count = {"LoggingMixin": 0, "CachingMixin": 0}


class LoggingMixinCounted:
    def __init__(self, **kwargs):
        init_count["LoggingMixin"] += 1
        print(f"  LoggingMixin.__init__ (call #{init_count['LoggingMixin']})")
        self.log = []
        super().__init__(**kwargs)

    def query(self):
        self.log.append("query")
        print(f"  LoggingMixin.query")
        super().query()


class CachingMixinCounted:
    def __init__(self, **kwargs):
        init_count["CachingMixin"] += 1
        print(f"  CachingMixin.__init__ (call #{init_count['CachingMixin']})")
        self.cache = {}
        super().__init__(**kwargs)

    def query(self):
        print(f"  CachingMixin.query")
        super().query()


class CachedLoggedDB_naive(
    LoggingMixinCounted, CachingMixinCounted, ThirdPartyDatabase
):
    def __init__(self, host, port):
        print(f"  CachedLoggedDB_naive.__init__")
        # You CAN'T just call super() here because ThirdPartyDatabase
        # breaks the chain. So you try direct calls instead:
        LoggingMixinCounted.__init__(self)  # direct call...
        # ^ BUT LoggingMixin uses super() internally!
        # Its super().__init__() follows the MRO: next is CachingMixin...
        # which then hits ThirdPartyDatabase with **kwargs → CRASH
        # There is NO way to mix direct calls with cooperative mixins cleanly.


print("MRO:", [c.__name__ for c in CachedLoggedDB_naive.__mro__])
print()
print("  Calling CachedLoggedDB_naive('db.example.com', 5432):")
print("  The cooperative mixins' super() chains COLLIDE with ThirdPartyDatabase:\n")
try:
    naive_db3 = CachedLoggedDB_naive("db.example.com", 5432)
except TypeError as e:
    print(f"  *** TypeError: {e}")
    print(f"\n  *** LoggingMixin called super().__init__(**kwargs) which")
    print(f"  *** followed the MRO to ThirdPartyDatabase — which has no **kwargs!")
    print(f"  *** There is NO clean way to mix direct-call and super() styles.")

# ── 3b. THE ADAPTER PATTERN — CORRECT SOLUTION ──────────────────────────────
#
# Hettinger's solution: wrap the third-party class in an Adapter
# that DOES use super() and DOES accept **kwargs.
#
# The adapter:
#   - inherits from a Root class (part of YOUR cooperative hierarchy)
#   - accepts **kwargs (to be a good cooperative citizen)
#   - instantiates the third-party class internally (composition)
#   - delegates method calls to the internal instance
#   - calls super() properly to keep the chain alive

print("\n" + "-" * 50)
print("[3b] The Adapter Pattern — CORRECT SOLUTION\n")


class Root:
    def query(self):
        assert not hasattr(
            super(), "query"
        ), "Unexpected 'query' method found — a class may be missing Root inheritance"
        print(f"  Root.query: end of chain ✓")

    def close(self):
        assert not hasattr(super(), "close"), "Unexpected 'close' method found"
        print(f"  Root.close: end of chain ✓")


class DatabaseAdapter(Root):
    def __init__(self, host, port, **kwargs):
        self._db = ThirdPartyDatabase(host, port)
        print(f"  DatabaseAdapter.__init__: wrapped ThirdPartyDatabase")
        super().__init__(**kwargs)

    def query(self):
        print(f"  DatabaseAdapter.query: delegating to ThirdPartyDatabase")
        self._db.query()
        super().query()

    def close(self):
        self._db.close()
        super().close()


class LoggingMixinFixed:
    def __init__(self, **kwargs):
        print(f"  LoggingMixin.__init__ running")
        self.log = []
        super().__init__(**kwargs)

    def query(self):
        self.log.append("query")
        print(f"  LoggingMixin.query: logged")
        super().query()


class CachingMixinFixed:
    def __init__(self, **kwargs):
        print(f"  CachingMixin.__init__ running")
        self.cache = {}
        super().__init__(**kwargs)

    def query(self):
        print(f"  CachingMixin.query: cache miss, fetching...")
        super().query()


class ProductionDB(LoggingMixinFixed, CachingMixinFixed, DatabaseAdapter):
    def __init__(self, host, port):
        print(f"  ProductionDB.__init__")
        super().__init__(host=host, port=port)


print("MRO of ProductionDB:", [c.__name__ for c in ProductionDB.__mro__])
print("\nProductionDB('prod.db.com', 5432):\n")
prod = ProductionDB("prod.db.com", 5432)

print(f"\n  Calling prod.query():\n")
prod.query()

print(f"\n  prod.log = {prod.log}")
print(f"  prod.cache = {prod.cache}")

# WHAT HAPPENS NOW:
#   ProductionDB.__init__
#     → LoggingMixin.__init__   (sets self.log)
#       → CachingMixin.__init__ (sets self.cache)
#         → DatabaseAdapter.__init__ (creates ThirdPartyDatabase internally)
#           → Root (chain terminates cleanly)
#
#   prod.query()
#     → LoggingMixin.query   (logs the call)
#       → CachingMixin.query (checks cache)
#         → DatabaseAdapter.query (delegates to ThirdPartyDatabase.query)
#           → Root.query (terminates)
#
# Every class runs EXACTLY ONCE.
# ThirdPartyDatabase never knew it was being cooperatively used.
# Its non-cooperative nature was hidden behind the adapter.

print()
