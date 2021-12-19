#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *crypto_sign_keypair_python(PyObject *self, PyObject *args)
{
    PyBytesObject *seed;
    uint8_t *pubkey;
    uint8_t *privkey;
    PyObject *private_key;
    PyObject *public_key;
    PyObject *rslt = PyTuple_New(2);

    if (!PyArg_ParseTuple(args, "S", &seed))
        return NULL;
    Py_DECREF(seed);

    pubkey = PyMem_Malloc(897);
    privkey = PyMem_Malloc(1281);

    crypto_sign_keypair(pubkey, privkey, (uint8_t *)PyBytes_AsString((PyObject*) seed));

    private_key = Py_BuildValue("y#", privkey, 1281);
    public_key = Py_BuildValue("y#", pubkey, 897);

    PyMem_Free(pubkey);
    PyMem_Free(privkey);

    PyTuple_SetItem(rslt,0,public_key);
    PyTuple_SetItem(rslt,1,private_key);

    return rslt;
}


static PyObject *crypto_sign_signature_python(PyObject *self, PyObject *args)
{
    PyBytesObject *m;
    PyBytesObject *sk;
    size_t mlen;
    uint8_t *sig;
    uint8_t *siglen;
    PyObject *output_sig;
    PyObject *sig_len;
    PyObject *rslt = PyTuple_New(2);

    // if (!PyArg_ParseTuple(args, "S", &seed))
    //     return NULL;
    // Py_DECREF(seed);

    // pubkey = PyMem_Malloc(897);
    // privkey = PyMem_Malloc(1281);

    // crypto_sign_signature(pubkey, privkey, (uint8_t *)PyBytes_AsString((PyObject*) seed));

    // private_key = Py_BuildValue("y#", privkey, 1281);
    // public_key = Py_BuildValue("y#", pubkey, 897);

    // PyMem_Free(pubkey);
    // PyMem_Free(privkey);

    // PyTuple_SetItem(rslt,0,public_key);
    // PyTuple_SetItem(rslt,1,private_key);

    return rslt;
}

static PyObject *crypto_sign_verify_python(PyObject *self, PyObject *args)
{
    PyBytesObject *seed;
    uint8_t *pubkey;
    uint8_t *privkey;
    PyObject *private_key;
    PyObject *public_key;
    PyObject *rslt = PyTuple_New(2);

    // if (!PyArg_ParseTuple(args, "S", &seed))
    //     return NULL;
    // Py_DECREF(seed);

    // pubkey = PyMem_Malloc(897);
    // privkey = PyMem_Malloc(1281);

    // crypto_sign_keypair(pubkey, privkey, (uint8_t *)PyBytes_AsString((PyObject*) seed));


    // private_key = Py_BuildValue("y#", privkey, 1281);
    // public_key = Py_BuildValue("y#", pubkey, 897);

    // PyMem_Free(pubkey);
    // PyMem_Free(privkey);

    // PyTuple_SetItem(rslt,0,public_key);
    // PyTuple_SetItem(rslt,1,private_key);

    return rslt;
}


static PyMethodDef tdc_falconMethods[] = {
    { "generate_keypair", crypto_sign_keypair_python, METH_VARARGS, "crypto_sign_keypair_python" },
//    { "sign", crypto_sign_signature_python, METH_VARARGS, "crypto_sign_signature_python" },
//    { "verify", crypto_sign_verify_python, METH_VARARGS, "crypto_sign_verify_python" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef tdc_falconModule = {
    PyModuleDef_HEAD_INIT,
    "crypto_sign_keypair",
//    "crypto_sign_signature_python",
//    "crypto_sign_verify_python",
    "...",
    -1,
    tdc_falconMethods
};

PyMODINIT_FUNC PyInit_tdc_falcon(void) {
    return PyModule_Create(&tdc_falconModule);
}
