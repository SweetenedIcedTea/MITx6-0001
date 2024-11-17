from p3 import sub

def test_sub():
    assert sub("azcbobobegghakl") == "beggh"
    assert sub("abcbcd") == "abc"
    assert sub("abcde") == "abcde"
    assert sub("zyxwvutsrqponmlkjihgfedcba") == "z"
    assert sub("a") == "a"
    assert sub("") == ""