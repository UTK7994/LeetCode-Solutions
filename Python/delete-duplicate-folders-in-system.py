# Time:  O(m * nlogn + l * t^2), m is the max number of folders in a path,
#                              , n is the number of paths
#                              , l is the max length of folder name
#                              , t is the size of trie
# Space: O(l * t^2)

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        def mark(node, lookup):
            serialized = "".join(child + mark(node[child], lookup) for child in sorted(node.iterkeys()) if child != "_del")
            if serialized:
                if serialized in lookup:
                    lookup[serialized]["_del"]
                    node["_del"]
                else:
                    lookup[serialized] = node
            return "(" + serialized + ")"
        
        def sweep(node, path, result):
            if path:
                result.append(path[:])
            for child in node.iterkeys():
                if "_del" in node[child]:
                    continue
                path.append(child)
                sweep(node[child], path, result)
                path.pop()

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for path in paths:
            reduce(dict.__getitem__, path, trie)
        lookup, result = {}, []
        mark(trie, lookup)
        sweep(trie, [], result)
        return result