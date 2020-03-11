__author__ = "Ben Carpenter", "Landon Stoner"

def load_int_list(filename):
    """ Reads a collection of integers stored in a text file 
        named filename. Stores the elements in a list in the 
        same order they appear in the file.  Returns the 
        list of elements. """
    f = open(filename)
    lin = f.read()
    line = lin.split()
    lines = [int(i) for i in line]
    f.close()
    return lines   # Replace with your implementation


def missing(checklist, mainlist):
    """ Returns the list containing all the elements of list 
        checklist that are not found in list mainlist.  If
        mainlist contains all the elements in checklist, the 
        function returns the empty list. This function does
        not modify the lists passed to it. """
    lst3 = []
    for i in checklist:
        if i not in mainlist:
            lst3.append(i)
    return lst3   # Replace with your implementation--do not use
                  # list comprehension


def missing2(checklist, mainlist):
    """ Returns the list containing all the elements of list 
        checklist that are not found in list mainlist.  If
        mainlist contains all the elements in checklist, the 
        function returns the empty list. This function does
        not modify the lists passed to it. """

    return [i for i in checklist if i not in mainlist]
                # statement that uses list comprehension


def rotate(lst, dist):
    """ Physically rearranges the elements of list lst, shifting 
        all the elements towards the back by the distance dist. 
        As an element "falls off" the rear, the function
        places it at the front in the space vacated when it shifted
        the first element backwards.

        For example, if list a contains the elements 
        [1, 2, 3, 4, 5, 6], the call rotate(a, 2) 
        rearranges the elements in a to contain [5, 6, 1, 2, 3, 4].
        Notice that if dist is equal to the length of the list, 
        after the rotation all the elements rotate to 
        their original locations.

        If dist is negative, the function shifts elements forward 
        dist spots instead of backwards. As an element "falls off" 
        the front the function places it on the rear in the space 
        vacated when it shifted the last element forwards.

        For example, if list a contains the elements 
        [1, 2, 3, 4, 5, 6], the call rotate(a list, -2) 
        rearranges list a to contain [3, 4, 5, 6, 1, 2]. 

        This function necessariy can modify the list passed by 
        the caller. """
    global lst1, lst2
    if dist >= 0:
        dis = len(lst)-dist
    elif dist < 0:
        dis = -len(lst)-dist
    if lst == lst1:
        lst1 = lst[dis:]+lst[:dis]
    elif lst == lst2:
        lst2 = lst[dis:]+lst[:dis]  # Replace with your implementation


def pairwise_sum(seq, n):
    """ Returns a list of 2-tuples (a, b) where a and b both
        are elements of list seq, a + b = n, and a <= b.  
        The list should contain no duplicate 2-tuples.  The 
        function returns the empty list if seq is empty, and
        the function's behavior is undefined if seq contains 
        at least one non-number. """
    lst3 = []
    lstchk = []
    done_once = False
    for i, i1 in enumerate(seq):
        if i1 * 2 == n and not done_once:
                    lst3.append((i1, i1))
                    done_once = True
        for i2 in seq[i+1:]:
            if i1 not in lstchk:
                if i1 + i2 == n and i1 < i2:
                    lst3.append((i1, i2))
                elif i1 + i2 == n and i2 < i1:
                    lst3.append((i2, i1))
        lstchk.append(i1)
    return lst3   # Replace with your implementation


def main():
    """ Exercises the load_int_list and missing functions with
        two small sample files."""
    global lst1, lst2
    # Get the file names from the user
    #file1 = input("Enter first file name: ")
    #file2 = input("Enter second file name: ")
    
    # Load the files' contents into their respective lists
    lst1 = load_int_list("list1.txt")  #file1, file2
    lst2 = load_int_list("list2.txt")
    # Determine the elements in lst1 that are missing from lst2
    mis = missing(lst1, lst2)
    mis2 = missing2(lst1, lst2)
    
    # Report the results
    print("Sequence 1:", lst1)
    print("Sequence 2:", lst2)
    print("Elements in sequence 1 missing from sequence 2:", mis)
    print("                                               ", mis2)

    # Rotate the lists
    rotate(lst1, 3)
    rotate(lst2, -5)
    print("Sequence 1 rotated 3:", lst1)
    print("Sequence 2 rotated -5:", lst2)

    # Exercise pairwise sums
    lst1 = list(range(0, 25))
    print("The pairwise sums to", 12, "in", lst1, "are")
    print("    ", pairwise_sum(lst1, 12))
    print("The pairwise sums to", 18, "in", lst1, "are")
    print("    ", pairwise_sum(lst1, 18))


if __name__ == "__main__":
    main()

