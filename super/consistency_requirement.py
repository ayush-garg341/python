# ─────────────────────────────────────────────────────────────────────────────
#  PART 2 — THE CONSISTENCY REQUIREMENT
# ─────────────────────────────────────────────────────────────────────────────
#
# THE RULE: If ANY class in a hierarchy uses super(), ALL of them must.
# A single class that doesn't call super() is a CHAIN BREAKER.
# Everything after it in the MRO is silently skipped — no error, no warning.
#
# There are two failure modes:
#   2a. A SUBCLASS doesn't use super() but its parents do  → double calls
#   2b. A CLASS IN THE MIDDLE doesn't use super()          → silent skipping
#
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("PART 2 — THE CONSISTENCY REQUIREMENT")
print("=" * 70)

# ── 2a. SUBCLASS BREAKS THE CONTRACT: causes DOUBLE CALLS ───────────────────
#
# Parents A and B use super(). But C's author doesn't know about super()
# and calls A.__init__ and B.__init__ directly.

print("\n[2a] When a SUBCLASS doesn't use super() — causes double calls\n")

call_log = []  # track every __init__ that runs


class P_A:
    def __init__(self):
        call_log.append("P_A")
        print(f"  P_A.__init__ running")
        super().__init__()  # uses super ✓


class P_B:
    def __init__(self):
        call_log.append("P_B")
        print(f"  P_B.__init__ running")
        super().__init__()  # uses super ✓


class P_C_bad(P_A, P_B):
    def __init__(self):
        call_log.append("P_C_bad")
        print(f"  P_C_bad.__init__ running — calling parents DIRECTLY")
        P_A.__init__(self)  # direct call — bypasses MRO
        P_B.__init__(self)  # direct call — bypasses MRO


print("MRO of P_C_bad:", [c.__name__ for c in P_C_bad.__mro__])
print("\nP_C_bad() — watch P_B run TWICE:\n")
call_log.clear()
P_C_bad()
print(f"\n  Call log: {call_log}")
print(f"  *** P_B ran {call_log.count('P_B')} time(s) — should be 1!")

# WHY P_B RUNS TWICE:
#   P_C_bad calls P_A.__init__ directly
#     → P_A uses super(), and P_B is next in MRO → P_B runs (1st time)
#   P_C_bad THEN calls P_B.__init__ directly → P_B runs AGAIN (2nd time!)
#
# This causes subtle, hard-to-find bugs:
#   - Database rows inserted twice
#   - Event handlers registered twice
#   - Counters incremented twice
#   - State mutated twice

print()

# Now let's see the CORRECT version — everyone uses super()


class P_C_good(P_A, P_B):
    def __init__(self):
        call_log.append("P_C_good")
        print(f"  P_C_good.__init__ running — using super()")
        super().__init__()  # super() chains correctly through the MRO


print("[2a-fixed] P_C_good() — everyone uses super():\n")
call_log.clear()
P_C_good()
print(f"\n  Call log: {call_log}")
print(f"  Each class ran exactly once. ✓")

# ── 2b. MIDDLE CLASS BREAKS THE CONTRACT: causes SILENT SKIPPING ────────────
#
# A more dangerous scenario: a class IN THE MIDDLE of the MRO
# doesn't call super(). Everything AFTER it is silently not called.
# There is NO error. You won't know unless you're looking.

print("\n" + "-" * 50)
print("[2b] When a MIDDLE CLASS doesn't use super() — causes silent skipping\n")


class M_A:
    def __init__(self):
        print(f"  M_A.__init__ running")
        super().__init__()  # uses super ✓


class M_B:
    def __init__(self):
        print(f"  M_B.__init__ running")
        # ← NO super() call here! Chain STOPS at M_B.


class M_C:
    def __init__(self):
        print(f"  M_C.__init__ running")
        super().__init__()  # uses super ✓ — but will never be reached!


class M_D(M_A, M_B, M_C):
    def __init__(self):
        print(f"  M_D.__init__ running")
        super().__init__()


print("MRO of M_D:", [c.__name__ for c in M_D.__mro__])
print("\nM_D() — watch M_C get silently skipped:\n")
M_D()
print("\n  *** M_C.__init__ was NEVER CALLED — and no error was raised!")

# WHAT HAPPENS:
#   M_D → super() → M_A   (calls super, passes to M_B)
#   M_A → super() → M_B   (M_B is next in MRO)
#   M_B → NO super() call → chain STOPS HERE
#   M_C is in the MRO but its __init__ is NEVER CALLED.
#
# This is the most insidious bug: imagine M_C was a SecurityMixin,
# a LoggingMixin, or a DatabaseConnectionMixin.
# It silently never runs. Your program continues without it.

print()

# ── 2c. WHY ORDERING DOESN'T SAVE YOU ───────────────────────────────────────
#
# You might think: "just put the non-cooperative class last in the MRO."
# This works for simple hierarchies but breaks when you compose them.

print("-" * 50)
print("[2c] Why 'put non-cooperative classes last' doesn't scale\n")


class Cooperative_1:
    def __init__(self, **kwargs):
        print(f"  Cooperative_1.__init__ running")
        super().__init__(**kwargs)


class NonCooperative:
    def __init__(self):
        print(f"  NonCooperative.__init__ running — NO super()")
        # no super() — chain ends here


# Each of these puts NonCooperative last — looks safe individually
class Sub1(Cooperative_1, NonCooperative):
    def __init__(self, **kwargs):
        print(f"  Sub1.__init__")
        super().__init__(**kwargs)


class Sub2(Cooperative_1, NonCooperative):
    def __init__(self, **kwargs):
        print(f"  Sub2.__init__")
        super().__init__(**kwargs)


print("MRO of Sub1:", [c.__name__ for c in Sub1.__mro__])
print("MRO of Sub2:", [c.__name__ for c in Sub2.__mro__])

# Now compose Sub1 and Sub2 together:
try:

    class Combined(Sub1, Sub2):
        pass

    print("MRO of Combined:", [c.__name__ for c in Combined.__mro__])
    # In this MRO, NonCooperative appears ONCE but it sits between
    # cooperative classes from Sub2 — the order rule breaks down.
except TypeError as e:
    print(f"  Cannot even create Combined: {e}")

# The fundamental lesson: you CANNOT consistently put non-cooperative
# classes "last" once you start composing subclasses of subclasses.
# The only real solution is: make everything cooperative.
