{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# this script is for creating the BIDS folder structure and standard file names based on the number of subjects in your neuroimaging study, enjoy!\n",
    "# import the os module\n",
    "import os\n",
    "\n",
    "# detect the current working directory and print it\n",
    "path = os.getcwd()\n",
    "print (\"The current working directory is %s\" % path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ls #listing files the files in the working dir"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# define the name of the directory to be created, checking access via creating some folders, setting working dir\n",
    "path = \"tmp/month/week\"\n",
    "\n",
    "try:\n",
    "    os.makedirs(path)\n",
    "except OSError:\n",
    "    print (\"Creation of the directory %s failed\" % path)\n",
    "else:\n",
    "    print (\"Successfully created the directory %s\" % path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Dogs=[\"Akira\",\"Alma\",\"Apacs\",\"Barack\",\"Barney\",\"Bodor\",\"Bodza\",\"Bran\",\"Buksi\",\"Csele\",\"Demi\",\"Floyd\",\"Grog\",\"Joey\",\"Kamilla\",\"Kara\",\"Kefir\",\"Kope\",\"Kosza\",\"Kunkun\",\"Luna\",\"Maverick\",\"Maya\",\"Mini\",\"Mirza\",\"Mokka\",\"Molly\",\"Monty\",\"Nia\",\"Odin\",\"Pan\",\"Sander\",\"Yuki\"]\n",
    "dogs=[]\n",
    "\n",
    "for s in Dogs:\n",
    "    z=s.lower()\n",
    "    dogs.append(z)\n",
    "\n",
    "dogs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#creating BIDS folder structure for all subjects\n",
    "for i in range(1,34):\n",
    "    Path(\"sub-\"+str(i).zfill(2)+\"/func\").mkdir(parents=True, exist_ok=True)\n",
    "    Path(\"sub-\"+str(i).zfill(2)+\"/anat\").mkdir(parents=True, exist_ok=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#creating new file names based on total no. of subjects\n",
    "subs=[]\n",
    "for i in range(1,34):\n",
    "    z=\"sub-\"+str(i).zfill(2)+\"_func_sub-\"+str(i).zfill(2)+\"_dog-rest_bold\"\n",
    "    subs.append(z)\n",
    "\n",
    "subs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#putting them together in a dict\n",
    "keys = dogs\n",
    "values = subs\n",
    "dictionary = dict(zip(keys, values))\n",
    "dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#adding some extra for session renaming\n",
    "dictionary.update({\"_rsfm_A_FH\": \"_run-01\", \"_rsfm_B_FH\" : \"_run-02\", \"wBBT_wr\":\"\"})\n",
    "dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#renaming the file after going through all the replacement steps in the filename string\n",
    "for fileName in os.listdir(\".\"):\n",
    "    address= fileName\n",
    "    for key in dictionary.keys():\n",
    "            address =address.replace(key, dictionary[key])\n",
    "    \n",
    "    os.rename(fileName, address)\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#checking that renaming run successfully\n",
    "os.listdir(\".\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
