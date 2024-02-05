import streamlit as st
import import_path as imp

imp.import_path("components")

from components import file_loader


def init():
    apply_components(st)


def apply_components(st):
    file_loader.apply(st)
