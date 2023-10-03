#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer to list head
 * @number: number to insert in new node
 *
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *curr;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	
	node->n = number;
	node->next = NULL;

	curr = *head;
	while (curr->next && curr->next->n < number)
		curr = curr->next;
	node->next = curr->next;
	curr->next = node;
	
	return (node);
}
