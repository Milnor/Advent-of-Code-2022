#!/usr/bin/env python3

def main():
    with open("./input/01-1.txt", "r") as file:
        all_data = file.readlines()
        #print(all_data)
        totals = []
        total = 0
        for item in all_data:
            if len(item) > 1:
                total += int(item.strip(), 10)
            else:
                totals.append(total)
                total = 0
        biggest = max(totals)
        index = totals.index(biggest)
        print(f"Elf #{index + 1} is carrying {biggest} calories.")

        # Total of the Top Three
        three_best = biggest
        totals.remove(biggest)
        three_best += max(totals)
        totals.remove(max(totals))
        three_best += max(totals)
        print(f"The total carried by the top three is {three_best}.")

if __name__ == "__main__":
    main()
