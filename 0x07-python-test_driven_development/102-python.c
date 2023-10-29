#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_string - prints info for python string
 *
 * @p: address of PyObject struct
 *
 * Returns: None
 */
void print_python_string(PyObject *p)
{
	/* print info */
	wprintf(L"[.] string object info\n");

	/* if invalid string object */
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}

	/* print type for ascii */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		wprintf(L"  type: compact ascii\n");
	else
		wprintf(L"  type: compact unicode object\n");

	/* print length and value of string */
	wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(p));
	wprintf(L"  value: %ls\n", PyUnicode_AS_UNICODE(p));
}
