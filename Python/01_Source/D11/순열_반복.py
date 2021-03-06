N = 3

arr = [1, 2, 3]

sel = [0] * N  # a리스트(내가 해당 원소를 뽑았는지 체크)


def powerset(idx):
    if idx == N:
        print(sel, ":", end=' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()

        return

    # idx자리의 원소를 뽑고 간다
    sel[idx] = 1
    powerset(idx + 1)

    # idx자리의 원소를 안뽑고 간다
    sel[idx] = 0
    powerset(idx + 1)


powerset(0)