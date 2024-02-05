import streamlit as st
import import_path as imp

imp.import_path("pages")

from pages import page


def init():
    apply_components(st)


def apply_components(st):
    page.apply(st)
