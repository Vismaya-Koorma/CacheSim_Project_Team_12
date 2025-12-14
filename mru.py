def mru_page_replacement(pages, capacity):
    memory = []
    recent = []   # to track most recently used pages
    page_faults = 0

    for page in pages:
        # Page Hit
        if page in memory:
            # update recent usage
            recent.remove(page)
            recent.append(page)
            print(f"Page {page} -> HIT | Memory: {memory}")

        # Page Fault
        else:
            page_faults += 1

            # If memory is full, remove MRU page
            if len(memory) == capacity:
                mru_page = recent.pop()  # most recently used
                memory.remove(mru_page)
                print(f"Page {mru_page} removed (MRU)")

            memory.append(page)
            recent.append(page)
            print(f"Page {page} -> FAULT | Memory: {memory}")

    print("\nTotal Page Faults:", page_faults)


# Driver Code
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
capacity = 3

mru_page_replacement(pages, capacity)
