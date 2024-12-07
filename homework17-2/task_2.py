def find_way(n, m):
    graph = {"A" : ["B", "C"], "B" : ["D"], "C" : ["E"]}
    
    if n in graph and m in graph[n]:
        return "There is a way"
    return "There is no way"
   
def main():
    print(find_way("A", "B"))
    print(find_way("G", "J"))

if __name__ == "__main__":
    main()