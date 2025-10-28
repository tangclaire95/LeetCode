class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans=0 
        cnt =Counter() #hashmap, char, int
        left=0
        for right, c in enumerate (s):
            cnt[c] +=1
            while cnt [c] >1:
                cnt [s[left]] -= 1
                left += 1
            ans =max(ans, right-left+1) #字符个数
        return ans 
#time o(n), space  o(1)

        