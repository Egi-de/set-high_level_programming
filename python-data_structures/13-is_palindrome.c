#include "lists.h"

/**
 * reverse_list - reverses a singly linked list in place
 * @head: pointer to the head of the list to reverse
 * Return: pointer to the new head (old tail)
 */
static listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *p1, *p2, *tail;
	int result = 1;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_list(slow);
	tail = second_half;

	p1 = *head;
	p2 = second_half;
	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			result = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	reverse_list(tail);

	return (result);
}
