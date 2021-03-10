import random
import os
import tempfile

import pytest

import parser


@pytest.fixture
def dummy_weight_file(request):
    total_weight = 0
    tmpfile = tempfile.mktemp()
    with open(tmpfile, "w") as f:
        for i in range(5):
            weight = random.randint(10, 100)
            total_weight += weight
            f.write(f"Jack : {weight}\n")
    yield tmpfile, total_weight
    os.unlink(tmpfile)
        
    
def test_total_weights(dummy_weight_file):
    f, expected_weight = dummy_weight_file
    actual_weight = parser.total_weights(f)
    assert actual_weight == expected_weight

        
