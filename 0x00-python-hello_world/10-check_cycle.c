#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a given linkedlist
 * @list: pointer to head of the linked list
 *
 * Return: 0 if there is no cycle, else 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list;
	listint_t *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
