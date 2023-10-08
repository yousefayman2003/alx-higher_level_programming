#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PyObject list
*/
void print_python_list_info(PyObject *p);
{
	PyObject *object;
	int length, size, i;

	/* getting length of list */
	length = Py_SIZE(p);
	/* getting size of allocated memory of list */
	size = ((PyListObject *)p)->allocated;

	/* print list info */
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", size);

	/* printing date types of in each index the list */
	for (i = 0; i < length; i++)
	{
		object = PyList_GetItem(p, i);
		char *type = Py_TYPE(object)->tp_name;

		printf("Element %d: %s\n", i, type);
	}
}
