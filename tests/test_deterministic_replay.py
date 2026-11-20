import pytest
from gameplay import deterministic_replay as mod

CASES = [
    ("sum", 'm.stable_sum([0.1, 0.2, 0.3]) == approx(0.6)'),
    ("seed", 'm.seed_for(1, 2) == 1103515247'),
    ("steps", 'm.fixed_steps(0.05, 0.02) == 2'),
    ("sort", 'm.sort_ids([3, 1, 2]) == [1, 2, 3]'),
    ("merge", 'm.merge_parallel([1, 2, 3]) == 6'),
    ("input", 'm.sample_input({1: "a"}, 1) == "a"'),
    ("ai", 'm.ai_decide(5, 999) == 5'),
    ("float", 'm.float_mode("ieee") is True'),
    ("diverge", 'm.first_divergence([1, 2, 3], [1, 9, 3]) == 1'),
    ("broad", 'm.broadphase_order(["b", "a"]) == ["a", "b"]'),
    ("acc", 'm.accumulate(0.05, 0.02, 0.0) == (2, 0.01)'),
    ("hash", 'm.replay_hash(["a", "b"]) == "a|b"'),
    ("snapshot", 'm.snapshot_every(4, 2) is True'),
    ("fill", 'm.fill_dropped([1, 2], 4) == (1, 2, None, None)'),
    ("id", 'm.replay_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
