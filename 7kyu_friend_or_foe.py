def friend(x):
    return [i for i in x if len(i) == 4]

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
        test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
        test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])