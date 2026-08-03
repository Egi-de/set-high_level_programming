#include <stdlib.h>
#include "lists.h"

/**
 * reverse_copy - creates a reversed copy of a listint_t list
 * @head: pointer to head of list
 * Return: pointer to head of reversed copy, or NULL if malloc fails
 */
listint_t *reverse_copy(listint_t *head)
{
	listint_t *new_head;
	listint_t *new_node;

	new_head = NULL;
	while (head != NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = head->n;
		new_node->next = new_head;
		new_head = new_node;
		head = head->next;
	}
	return (new_head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of list
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed;
	listint_t *original;
	listint_t *tmp;
	int result;

	if (head == NULL || *head == NULL)
		return (1);

	reversed = reverse_copy(*head);
	if (reversed == NULL && *head != NULL)
		return (0);

	original = *head;
	result = 1;
	while (original != NULL && reversed != NULL)
	{
		if (original->n != reversed->n)
		{
			result = 0;
			break;
		}
		original = original->next;
		reversed = reversed->next;
	}

	while (reversed != NULL)
	{
		tmp = reversed->next;
		free(reversed);
		reversed = tmp;
	}

	return (result);
}
