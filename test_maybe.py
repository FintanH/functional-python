__author__ = 'halpenny'
from monad.maybe import Just, Nothing, do, is_just, is_nothing, from_just, list_to_maybe, map_maybe, cat_maybes, maybe

def head(lis):

    if len(lis):
        return Just(lis[0])
    else:
        return Nothing()


def plus_one(x):
    return Just(x + 1)


test_list = []
test_list_2 = [1, 2, 3, 4]

print do(test_list_2, head, plus_one)

res = head(test_list).bind(plus_one)
res_1 = head(test_list_2).bind(plus_one)

print maybe(-1, plus_one, res)
print maybe(1, plus_one, res_1)

print is_just(res)
print is_nothing(res)

print is_just(res_1)
print is_nothing(res_1)

print from_just(res_1)

print list_to_maybe([1, 2, 3, 4])
print list_to_maybe([])

print cat_maybes([Just(1), Just(2), Just(3), Nothing()])

list_of_lists = [[1, 2], [], [5, 6]]

print map_maybe(head, list_of_lists)