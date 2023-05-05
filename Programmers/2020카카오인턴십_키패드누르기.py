def solution(numbers, hand):
    answer = ''

    left = [4, 1]
    right = [4, 3]
    for num in numbers:
        if num == 1:
            left = [1, 1]
            answer += 'L'
        elif num == 4:
            left = [2, 1]
            answer += 'L'
        elif num == 7:
            left = [3, 1]
            answer += 'L'
        elif num == 3:
            right = [1, 3]
            answer += 'R'
        elif num == 6:
            right = [2, 3]
            answer += 'R'
        elif num == 9:
            right = [3, 3]
            answer += 'R'
        elif num == 2:
            if abs(left[0] - 1) + abs(left[1] - 2) < abs(right[0] - 1) + abs(right[1] - 2):
                left = [1, 2]
                answer += 'L'
            elif abs(left[0] - 1) + abs(left[1] - 2) > abs(right[0] - 1) + abs(right[1] - 2):
                right = [1, 2]
                answer += 'R'
            else:
                if hand == 'left':
                    left = [1, 2]
                    answer += 'L'
                else:
                    right = [1, 2]
                    answer += 'R'
        elif num == 5:
            if abs(left[0] - 2) + abs(left[1] - 2) < abs(right[0] - 2) + abs(right[1] - 2):
                left = [2, 2]
                answer += 'L'
            elif abs(left[0] - 2) + abs(left[1] - 2) > abs(right[0] - 2) + abs(right[1] - 2):
                right = [2, 2]
                answer += 'R'
            else:
                if hand == 'left':
                    left = [2, 2]
                    answer += 'L'
                else:
                    right = [2, 2]
                    answer += 'R'
        elif num == 8:
            if abs(left[0] - 3) + abs(left[1] - 2) < abs(right[0] - 3) + abs(right[1] - 2):
                left = [3, 2]
                answer += 'L'
            elif abs(left[0] - 3) + abs(left[1] - 2) > abs(right[0] - 3) + abs(right[1] - 2):
                right = [3, 2]
                answer += 'R'
            else:
                if hand == 'left':
                    left = [3, 2]
                    answer += 'L'
                else:
                    right = [3, 2]
                    answer += 'R'
        else:
            if abs(left[0] - 4) + abs(left[1] - 2) < abs(right[0] - 4) + abs(right[1] - 2):
                left = [4, 2]
                answer += 'L'
            elif abs(left[0] - 4) + abs(left[1] - 2) > abs(right[0] - 4) + abs(right[1] - 2):
                right = [4, 2]
                answer += 'R'
            else:
                if hand == 'left':
                    left = [4, 2]
                    answer += 'L'
                else:
                    right = [4, 2]
                    answer += 'R'

    return answer