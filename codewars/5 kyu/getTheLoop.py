# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def loop_size(node, cnt=0, nodes={}):
  while True:
    nodes[node] = cnt
    if node.next in nodes:
        return cnt - nodes[node.next] + 1
    node = node.next
    cnt += 1
