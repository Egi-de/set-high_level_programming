#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <string.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about a Python list
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyListObject *list = (PyListObject *)p;

    size = list->ob_base.ob_size;
    alloc = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", (long)size);
    printf("[*] Allocated = %ld\n", (long)alloc);

    for (i = 0; i < size; i++)
    {
        PyObject *item = list->ob_item[i];
        printf("Element %ld: %s\n", (long)i, item->ob_type->tp_name);
        if (strcmp(item->ob_type->tp_name, "bytes") == 0)
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - prints basic info about a Python bytes object
 * @p: PyObject pointer to the bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i, limit;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");

    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = bytes->ob_base.ob_size;
    printf("  size: %ld\n", (long)size);
    printf("  trying string: %s\n", bytes->ob_sval);

    limit = size + 1;
    if (limit > 10)
        limit = 10;

    printf("  first %ld bytes: ", (long)limit);
    for (i = 0; i < limit; i++)
    {
        printf("%02x", (unsigned char)bytes->ob_sval[i]);
        if (i < limit - 1)
            printf(" ");
    }
    printf("\n");
}