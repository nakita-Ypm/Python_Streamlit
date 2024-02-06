import streamlit as st
import xml.etree.ElementTree as ET

import import_path as imp

imp.import_path("components/xml_load")

from components.xml_load import xml_load

st.title("XML Reader App")

xml_load.apply()
