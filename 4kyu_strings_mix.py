import re

def mix(s1, s2):
    s1 = sorted(re.sub('[^a-z]+', '', s1))
    s2 = sorted(re.sub('[^a-z]+', '', s2))
    counts = {'1':{},'2':{}, '=':{}}
    diff = []
    ptr = 0
    temp = ''
    while ptr < len(s1):
        if(s1[ptr] != temp):
            counts['1'][s1[ptr]] = s1.count(s1[ptr])
            temp = s1[ptr]
        ptr += 1
    ptr = 0
    temp = ''

    while ptr < len(s2):
        if(s2[ptr] != temp):
            if not s2[ptr] in counts['1']:
                counts['2'][s2[ptr]] = s2.count(s2[ptr])
            elif counts['1'][s2[ptr]] < s2.count(s2[ptr]):
                counts['2'][s2[ptr]] = s2.count(s2[ptr])
                del counts['1'][s2[ptr]]
            elif counts['1'][s2[ptr]] == s2.count(s2[ptr]):
                counts['='][s2[ptr]] = s2.count(s2[ptr])
                del counts['1'][s2[ptr]]
            temp = s2[ptr]
        ptr += 1

    for val in counts['1']:
        if(counts['1'][val] > 1):
            diff.append('1:' + counts['1'][val] * val)

    for val in counts['2']:
        if (counts['2'][val] > 1):
            diff.append('2:' + counts['2'][val] * val)

    for val in counts['=']:
        if (counts['='][val] > 1):
            diff.append('=:' + counts['='][val] * val)

    diff = sorted(diff, key=len, reverse=True)
    return ('/'.join(diff))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        test.assert_equals(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
                           '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"),
                           "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        test.assert_equals(mix(" In many languages", " there's a pair of functions"),
                           "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        test.assert_equals(mix("codewars", "codewars"), "")
        test.assert_equals(mix("A generation must confront the looming ", "codewarrs"),
                           "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")