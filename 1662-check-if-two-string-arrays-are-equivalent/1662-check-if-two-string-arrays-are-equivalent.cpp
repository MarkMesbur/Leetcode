class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        return concat(word1) == concat(word2);
    }
    
    string concat(vector<string>& strings){
        string s;
        for (vector<string>::iterator t=strings.begin(); t!=strings.end(); ++t) 
    {
        s += *t;
    }
        return s;
    }
};