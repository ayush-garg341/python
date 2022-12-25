"""
Given an input array of scores for students in an exam, professor wants to give grade to each student. He wants to give mminimum of one to each.
But there is a rule. The grade of student must be greater than adjacent student if the student has lower score.
Similarly the grade of student must be lower than adjacent student if the student has higher score.

Find the minimum rewards that professor can give.

example1:
    input -> [8, 4, 2, 1, 3, 6, 7, 9, 5]
    output -> [4, 3, 2, 1, 2, 3, 4, 5, 1]
"""


def minRewards(scores):
    """
    TC -> O(n^2), Naive approach
    Space Complexity -> O(n)
    """
    min_rewards = [0 for i in range(len(scores))]
    min_rewards[0] = 1

    for i in range(1, len(scores)):
        if scores[i] < scores[i - 1]:
            # backtrack and increment the count
            min_rewards[i] = 1
            end = i - 1
            while end >= 0:
                if scores[end] < scores[end + 1]:
                    break
                else:
                    # handles the edge case
                    if end > 0 and scores[end] > scores[end - 1]:
                        if min_rewards[end] <= min_rewards[end + 1]:
                            min_rewards[end] = min_rewards[end + 1] + 1
                    else:
                        min_rewards[end] += 1

                end -= 1

        else:
            min_rewards[i] = min_rewards[i - 1] + 1
    return sum(min_rewards)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
print(minRewards([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]))
print(
    minRewards(
        [
            800,
            400,
            20,
            10,
            30,
            61,
            70,
            90,
            17,
            21,
            22,
            13,
            12,
            11,
            8,
            4,
            2,
            1,
            3,
            6,
            7,
            9,
            0,
            68,
            55,
            67,
            57,
            60,
            51,
            661,
            50,
            65,
            53,
        ]
    )
)
print(minRewards([0, 4, 2, 1, 3]))
