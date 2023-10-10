#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * get_list_length - Get the length of a linked list
 * @head: A pointer to a pointer to the head of the list
 *
 * Description: This function calculates the length of a linked list by
 * iterating through it and counting the nodes.
 *
 * Return: The length of the linked list as a size_t.
 */
size_t get_list_length(listint_t **const head)
{
	size_t len = 0;
	listint_t *current = *head;

	for (; current; current = current->next)
		len++;
	return (len);
}

/**
 * convert_llist_to_array - Convert a linked list to an integer array
 * @head: A pointer to a pointer to the head of the list
 * @size: The size of the linked list
 *
 * Description: This function converts a linked list of integers to an
 * integer array. It allocates memory for the array and copies the list
 * elements into it.
 *
 * Return: A pointer to the newly allocated integer array.
 */
int *convert_llist_to_array(listint_t **const head, size_t size)
{
	int *arr;
	size_t i;
	listint_t *current = *head;

	arr = malloc(sizeof(int) * size);
	if (!arr)
		exit(1);
	for (i = 0; current; (current = current->next))
		arr[i++] = current->n;

	return (arr);
}

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: A pointer to a pointer to the head of the list
 *
 * Description: This function checks if a linked list of integers is a
 * palindrome by converting it to an array and comparing elements from
 * the beginning and end.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	if (!(*head))
		return (1);

	size_t size = get_list_length(head);
	int left = 0, right = size - 1, keep_going = 1, *arr;

	arr = convert_llist_to_array(head, size);
	while (left <= right && keep_going)
		if (arr[left++] != arr[right--])
			keep_going = 0;
	free(arr);
	return (keep_going);

}
