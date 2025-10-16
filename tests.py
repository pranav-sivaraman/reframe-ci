import reframe as rfm
import reframe.core.builtins as builtins
from reframe.core.meta import make_test

test_configs: dict = {
    "foo": {"num_nodes": [1], "ppn": [-1]},
    "bar": {"num_nodes": [1], "ppn": [-1]},
    "baz": {"num_nodes": [1], "ppn": [-1]},
}

tests = []
for test_name, config in test_configs.items():
    tests.append(
        make_test(
            f"{test_name}",
            (rfm.RunOnlyRegressionTest,),
            {
                "valid_systems": ["*"],
                "valid_prog_environs": ["*"],
                "executable": f"echo {test_name}",
                "num_nodes": builtins.parameter(config["num_nodes"], type=int),
                "ppn": builtins.parameter(config["ppn"], type=int),
                # "time_limit": config["time_limit"],
                # "sanity_patterns": sn.assert_true(1),
            },
        )
    )

for test in tests:
    rfm.simple_test(test)
