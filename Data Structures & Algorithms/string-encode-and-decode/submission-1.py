class Solution:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        # Use a length-prefix + delimiter strategy: "5#hello5#world"
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        res, i = [], 0
        
        while i < len(s):
            # 1. Find the delimiter '#' starting from index i
            j = s.find("#", i)
            
            # 2. Convert the text before '#' into an integer (the length)
            length = int(s[i:j])
            
            # 3. Extract the string using the length (starting after the '#')
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. Move the pointer to the start of the next encoded chunk
            i = end
            
        return res