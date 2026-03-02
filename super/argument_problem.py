# ─────────────────────────────────────────────────────────────────────────────
#  PART 1 — THE ARGUMENT PROBLEM
# ─────────────────────────────────────────────────────────────────────────────
#
# THE SCENARIO
# ------------
# You have a diamond-like hierarchy:
#
#         object
#        /      \
#       A        B
#        \      /
#          C
#
# A.__init__ takes no extra args.
# B.__init__ takes a positional arg.
# C inherits from both A and B.
#
# THE TRAP
# --------
# When you call C(), Python builds the MRO:  C → A → B → object
# A's super() call doesn't go to A's parent (object).
# It goes to B — because B is next in C's MRO.
# But A was written to pass NO arguments. B expects one. BOOM.
#
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("PART 1 — THE ARGUMENT PROBLEM")
print("=" * 70)

# ── 1a. THE BROKEN VERSION ──────────────────────────────────────────────────


class A_broken:
    def __init__(self):
        print(f"  A_broken.__init__ called")
        # A was written thinking it only needs to call object.__init__
        # But in the MRO of C_broken, the next class after A is B_broken!
        # And B_broken requires a 'value' argument that we're NOT passing.
        super().__init__()  # ← passes NOTHING — this will crash if B is next


class B_broken:
    def __init__(self, value):  # ← requires a positional argument
        print(f"  B_broken.__init__ called, value={value}")
        super().__init__()


class C_broken(A_broken, B_broken):
    def __init__(self, value):
        print(f"  C_broken.__init__ called, value={value}")
        super().__init__(value)  # passes value to A... but A drops it


print("\n[1a] MRO of C_broken:", [c.__name__ for c in C_broken.__mro__])
print("[1a] Attempting C_broken(42) — this will CRASH:\n")
try:
    C_broken(42)
except TypeError as e:
    print(f"  *** TypeError: {e}")

# WHY IT CRASHES:
#   C_broken(42)
#     → calls A_broken.__init__()  ← value=42 is DROPPED by A
#       → A calls super().__init__()  ← passes NOTHING
#         → MRO says next is B_broken
#           → B_broken.__init__() requires value — but got nothing → CRASH

print()

# ── 1b. THE WRONG FIX (just passing *args) ──────────────────────────────────


class A_partial_fix:
    def __init__(self, *args, **kwargs):
        print(f"  A_partial_fix.__init__ called, args={args}")
        # We accept *args now — but we SWALLOW them instead of forwarding
        super().__init__()  # ← still drops args! doesn't pass to next in MRO


class B_partial_fix:
    def __init__(self, value):
        print(f"  B_partial_fix.__init__ called, value={value}")
        super().__init__()


class C_partial_fix(A_partial_fix, B_partial_fix):
    def __init__(self, value):
        print(f"  C_partial_fix.__init__ called")
        super().__init__(value)


print("[1b] MRO of C_partial_fix:", [c.__name__ for c in C_partial_fix.__mro__])
print("[1b] Attempting C_partial_fix(42) — still CRASHES:\n")
try:
    C_partial_fix(42)
except TypeError as e:
    print(f"  *** TypeError: {e}")

print()

# ── 1c. THE CORRECT FIX: *args/**kwargs forwarding ──────────────────────────
#
# The rule: Every class in the chain must:
#   1. Accept *args and **kwargs (to absorb unknown arguments)
#   2. FORWARD them untouched via super().__init__(*args, **kwargs)
#
# This way arguments flow through the entire chain like a relay baton,
# and each class can use what it needs without breaking the chain.


class A_fixed:
    def __init__(self, *args, **kwargs):
        print(f"  A_fixed.__init__ called, forwarding args={args} kwargs={kwargs}")
        super().__init__(*args, **kwargs)  # ← FORWARD everything


class B_fixed:
    def __init__(self, value, *args, **kwargs):  # ← takes 'value' + absorbs rest
        print(f"  B_fixed.__init__ called, value={value}")
        super().__init__(*args, **kwargs)


class C_fixed(A_fixed, B_fixed):
    def __init__(self, value):
        print(f"  C_fixed.__init__ called, value={value}")
        super().__init__(value)


print("[1c] MRO of C_fixed:", [c.__name__ for c in C_fixed.__mro__])
print("[1c] C_fixed(42) — WORKS:\n")
C_fixed(42)

print()

# ── 1d. THE BEST PRACTICE: keyword-only arguments ───────────────────────────
#
# Even better: use KEYWORD-ONLY arguments everywhere.
# Each class pulls out what it needs from **kwargs, passes the rest along.
# This is Hettinger's recommended style.


class Shape:
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        print(f"  Shape.__init__: shapename={shapename}, remaining kwargs={kwargs}")
        super().__init__(**kwargs)  # forward whatever is left


class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        print(f"  ColoredShape.__init__: color={color}, remaining kwargs={kwargs}")
        super().__init__(**kwargs)  # 'color' consumed, forward rest


class SizedShape(ColoredShape):
    def __init__(self, size, **kwargs):
        self.size = size
        print(f"  SizedShape.__init__: size={size}, remaining kwargs={kwargs}")
        super().__init__(**kwargs)  # 'size' consumed, forward rest


print("[1d] MRO of SizedShape:", [c.__name__ for c in SizedShape.__mro__])
print("[1d] SizedShape(size='large', color='red', shapename='circle'):\n")
s = SizedShape(size="large", color="red", shapename="circle")
print(f"\n  Result: size={s.size}, color={s.color}, shapename={s.shapename}")

# HOW IT WORKS:
#   SizedShape pulls 'size' out, passes {color, shapename} to ColoredShape
#   ColoredShape pulls 'color' out, passes {shapename} to Shape
#   Shape pulls 'shapename' out, passes {} to object
#   object.__init__() receives an empty dict — exactly what it wants
#   Nobody crashes. Nobody drops data. The chain is unbroken.
