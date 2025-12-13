def lfu_page_replacement():
    # User inputs
    memory_size = int(input("Enter memory size: "))
    cache_size = int(input("Enter cache (frame) size: "))

    reference_string = list(map(int, input("Enter page reference string (space-separated): ").split()))

    # Data structures
    cache = []
    frequency = {}
    page_faults = 0

    print("\nPage\tCache\t\tFault")

    for page in reference_string:
        fault = False

        # If page is not in cache → page fault
        if page not in cache:
            page_faults += 1
            fault = True

            # If cache has space
            if len(cache) < cache_size:
                cache.append(page)
                frequency[page] = 1
            else:
                # Find LFU page
                lfu_page = min(cache, key=lambda x: frequency[x])
                
                # Replace LFU page
                cache.remove(lfu_page)
                del frequency[lfu_page]

                cache.append(page)
                frequency[page] = 1
        else:
            # Page hit → increase frequency
            frequency[page] += 1

        print(f"{page}\t{cache}\t\t{'Yes' if fault else 'No'}")

    print("\nTotal Page Faults:", page_faults)


if __name__ == "__main__":
    lfu_page_replacement()