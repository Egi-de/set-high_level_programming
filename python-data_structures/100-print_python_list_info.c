#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about a Python list
 * @p: PyObject pointer to the list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = (PyListObject *)p;

	size = Py_SIZE(list);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
