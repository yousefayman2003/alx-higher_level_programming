#include <object.h>
#include <listobject.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PyObject list
*/
void print_python_list_info(PyObject *p)
{
	int i;
	/* getting length of list */
	long int size = PyList_Size(p);
	/* making a pylist object */
	PyListObject *object = (PyListObject *)p;

	/* print list info */
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);

	/* printing date types of in each index the list */
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(objecy->ob_item[i])->tp_name);
}
