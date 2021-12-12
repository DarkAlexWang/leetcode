class FetchItemsToDisplay(object):
    #sort_column: int, sort_order: int, results_per_page: int, page_ind
    #ex: int, results: Dict[str, Tuple[int, int]])
    def solution(self,URLS, sort_column, sort_order, results_per_page, page_index):
            ordered = []
            for name in URLS:
                ordered.append((name,URLS[name][0],URLS[name][1]))
            ordered.sort(key=lambda x: x[sort_column], reverse=(sort_order == False))
            start_index = results_per_page * page_index
            return [name for name, _, _ in ordered[start_index:start_index + results_per_page]]
if __name__ == "__main__":
    display = FetchItemsToDisplay()
    res1 = display.solution({'p1':(10,5),'p2':(3,3),'p3':(17,4),'p4':(9 ,4),'p5':(1,5)},1,False,3,1)
    print (res1)
    res2 = display.solution({"foo.com":(10, 15), "bar.com":(3, 4),"baz. com":(17, 8)},1,False,2,1)
    print (res2)


#from typing import Dict, List, Tuple
#
#def fetch_results_to_display(sort_column: int, sort_order: int, results_per_page: int, page_index: int, results: Dict[str, Tuple[int, int]]) -> List[str]:
#    ordered = [(name, rel, price) for name, (rel, price) in results.items()]
#    # sort by sort_column and reverse order if needed
#    ordered.sort(key=lambda x: x[sort_column], reverse= sort_order == 1)
#    # find the start index of the first result on the target page
#    start_index = results_per_page * page_index
#    # return only the name of each result on the page
#    return [name for name, _, _ in ordered[start_index:start_index + results_per_page]]
#
#if __name__ == '__main__':
#    sort_column = int(input())
#    sort_order = int(input())
#    results_per_page = int(input())
#    page_index = int(input())
#    results_length = int(input())
#    results = {
#        n: (int(r), int(p))
#        for _ in range(results_length)
#        for n, r, p in [input().split()]
#    }
#    res = fetch_results_to_display(sort_column, sort_order, results_per_page, page_index, results)
#    print(' '.join(res))
