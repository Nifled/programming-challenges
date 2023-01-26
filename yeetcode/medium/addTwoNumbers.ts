// https://leetcode.com/problems/add-two-numbers/

// Definition for singly-linked list.
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(value?: number, next?: ListNode | null) {
    this.val = value === undefined ? 0 : value;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null,
  carried = 0 // carry over sum
): ListNode | null {
  const numA = l1?.val || 0;
  const numB = l2?.val || 0;
  const digitSum = numA + numB + carried;

  const placeTotal = digitSum % 10; // if `digitSum` is > 10, this will be a remainder and carry over
  const carry = Math.floor(digitSum / 10); // EG: `digitSum` = 18. carry is 1 and remainder is 8

  if (!l1?.next && !l2?.next) {
    // if last `digitSum` is > 10, create two final nodes for each digit.
    // EG: `digitSum` = 18, last nodes will look like (8)->(1)
    if (digitSum >= 10) {
      return new ListNode(placeTotal, new ListNode(1));
    }
    return new ListNode(digitSum);
  }

  // Recursively calculate the rest of the nodes sums and carrying over 10 if needed
  return new ListNode(
    placeTotal,
    addTwoNumbers(l1 ? l1.next : null, l2 ? l2.next : null, carry)
  );
}
