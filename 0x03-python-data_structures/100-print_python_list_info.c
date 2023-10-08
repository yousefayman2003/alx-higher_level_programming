#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PyObject list
*/
void print_python_list_info(PyObject *p)
{
	/* getting length of list */
	long int size = PyList_Size(p);
	/* making a pylist object */
	PyListObject *obj = (PyListObject *)p;
	int i;

	/* print list info */
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	/* printing date types of in each index the list */
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
