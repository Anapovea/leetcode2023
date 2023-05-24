# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:       
        
        #convert to string
        num1=""
        num2=""
        while l1:
            num1=num1+str(l1.val)  #value
            l1=l1.next   #next
        while l2:
            num2+=str(l2.val)
            l2=l2.next        
        
        sumi=str(int(num1)+int(num2)) # sum and convert to string to be iterable in for
        sm=str(int((num1)[::-1])+int((num2)[::-1]))[::-1]
        sumi_reversed = sumi[::-1]   # reverse the string  #this solution is wrong because the reverse must be before
        print(sumi_reversed)
        
        final=ListNode(0)  #create and empty ListNode
        tmp = final
        print(tmp)
        for j in sm:
            print(j)  #7,0,8
            tmp.next = ListNode(int(j)) #convert to int (from string)
            print(tmp.next)
            tmp=tmp.next
        return (final.next)
        
             
