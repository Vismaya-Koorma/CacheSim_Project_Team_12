def lru(pages, frames):
    memory = []
    page_faults = 0

    print("\n--- LRU Page Replacement ---")
    for p in pages:

        
        if p in memory:
            memory.remove(p)
            memory.append(p)

        else:
            
            page_faults += 1

            
            if len(memory) < frames:
                memory.append(p)
            else:
                
                memory.pop(0)
                memory.append(p)

        print(f"Page {p}: {memory}")

    return page_faults


def main():
    print("\n============== LRU PAGE REPLACEMENT ==============")

    
    pages = list(map(int, input("Enter page reference string (space-separated): ").split()))

    
    frames = int(input("Enter number of frames: "))


    faults = lru(pages, frames)

    print(f"\nTotal Page Faults (LRU): {faults}")


if __name__ == "__main__":
    main()
