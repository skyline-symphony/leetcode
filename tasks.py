# 3637. Trionic Array I
#An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#nums[0...p] is strictly increasing,
#nums[p...q] is strictly decreasing,
#nums[q...n − 1] is strictly increasing.
#Return true if nums is trionic, otherwise return false.

def isTrionic(nums: list[int]) -> bool:
        if len(nums) < 4:
            return False
        else:
            ans = []
            check = 0
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    if check == 0 or check == -1:
                        ans.append(1)
                    check = 1
                elif nums[i] < nums[i-1]:
                    if check == 0 or check == 1:
                        ans.append(-1)
                    check = -1
                else:
                     return False
        if ans == [1, -1, 1]:
            return True
        else:
            return False


#601. Human Traffic of Stadium
#Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
#Return the result table ordered by visit_date in ascending order.
#The result format is in the following example.

with temp as (select id, row_number() over(order by id)  as rn,
id - row_number() over(order by id) as dif,
visit_date, people
from stadium
where people >= 100),
difs as (select dif, count(dif) as cnt from temp group by dif)
select id, visit_date, people from temp where dif in (select dif from difs where cnt >= 3);
