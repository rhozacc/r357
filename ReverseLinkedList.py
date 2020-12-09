# a -> b -> c -> d -> None
# d -> c -> b -> a -> None

def reverseLinkedList(head):
	new_head = None
	curr = head
	previous = None # we need it because we need to set it to None
	while True:
		# next_guy = head.next
		# next_next_guy = next_guy.next
		# next_guy.next = curr
		# tmp_previous = curr.next
		if not curr.next:
			break

		# b | c
		tmp_curr = curr.next
		# a - > None | b -> a
		curr.next = previous
		# a | b
		previous = curr

		if not tmp_curr:
			break

		# b | c
		curr = tmp_curr

	return curr


x“