def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').split()).strip()

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(song_decoder("AWUBBWUBC"), "A B C", "WUB should be replaced by 1 space")
        test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C",
                           "multiples WUB should be replaced by only 1 space")
        test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C", "heading or trailing spaces should be removed")