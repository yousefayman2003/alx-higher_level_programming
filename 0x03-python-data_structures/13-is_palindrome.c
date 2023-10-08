#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of head of a given linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *curr = *head;
	listint_t *prev = NULL;
	listint_t *tmp;

	if (!head || !(*head))
		return (1);

	/* get middle of linked list */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* reverse linked list after middle */
	while (slow)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	/* check if linked list is palindrome */
	while (prev)
	{
		if (curr->n != prev->n)
			return (0);
		curr = curr->next;
		prev = prev->next;
	}
	return (1);
}
