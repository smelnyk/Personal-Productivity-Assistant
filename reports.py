"""
This module provides functions to generate reports for application and website usage.
"""

from file_loaders import load_csv_log_files
from file_loaders import load_productive_list, load_unproductive_list
from utils import load_csv_to_dict, humanize_time
from ollamas import get_classified_items, get_analysis

def generate_today_report():
    """
    Generate a report for today's application and website usage.

    This function loads the log files for the current day, classifies the applications
    into productive, unproductive, and unclassified categories, and then uses AI to
    auto-classify the unclassified applications. Finally, it generates an analysis report.

    Returns:
        str: The analysis report in Markdown format.
    """
    log_dict = load_csv_log_files(current_day_only=True)
    log_dict = dict(sorted(log_dict.items(), key=lambda item: item[1], reverse=True))

    productive_names = load_productive_list()
    unproductive_names = load_unproductive_list()

    productive_apps = {}
    unproductive_apps = {}
    unclassified_apps = {}

    for app_name, time_spent in log_dict.items():
        if any(productive_app in app_name for productive_app in productive_names):
            productive_apps[app_name] = humanize_time(time_spent)
        elif any(unproductive_app in app_name for unproductive_app in unproductive_names):
            unproductive_apps[app_name] = humanize_time(time_spent)
        else:
            unclassified_apps[app_name] = humanize_time(time_spent)

    try:
        ai_results = get_classified_items("\n".join([f"{i},{item}" for i, item in enumerate(unclassified_apps.keys())]))
        ai_results_dict = load_csv_to_dict(ai_results)
    except Exception as e:
        print(f"Error: {e}")
        ai_results = get_classified_items("\n".join([f"{i},{item}" for i, item in enumerate(unclassified_apps.keys())]))
        ai_results_dict = load_csv_to_dict(ai_results)

    for app_name, classified_type in ai_results_dict.items():
        if classified_type == "productive" and app_name in unclassified_apps:
            productive_apps[app_name] = unclassified_apps[app_name]
        elif classified_type == "unproductive" and app_name in unclassified_apps:
            unproductive_apps[app_name] = unclassified_apps[app_name]

    try:
        return get_analysis(productive_apps, unproductive_apps)
    except Exception as e:
        print(f"Error: {e}")
        return get_analysis(productive_apps, unproductive_apps)


def generate_all_time_report():
    """
    Generate a report for all-time application and website usage.

    This function loads all log files, classifies the applications into productive,
    unproductive, and unclassified categories, and then uses AI to auto-classify the
    unclassified applications. Finally, it generates an analysis report.

    Returns:
        str: The analysis report in Markdown format.
    """
    log_dict = load_csv_log_files(current_day_only=False)
    log_dict = dict(sorted(log_dict.items(), key=lambda item: item[1], reverse=True))

    productive_names = load_productive_list()
    unproductive_names = load_unproductive_list()

    productive_apps = {}
    unproductive_apps = {}
    unclassified_apps = {}

    for app_name, time_spent in log_dict.items():
        if any(productive_app in app_name for productive_app in productive_names):
            productive_apps[app_name] = humanize_time(time_spent)
        elif any(unproductive_app in app_name for unproductive_app in unproductive_names):
            unproductive_apps[app_name] = humanize_time(time_spent)
        else:
            unclassified_apps[app_name] = humanize_time(time_spent)

    try:
        ai_results = get_classified_items("\n".join(unclassified_apps.keys()))
        ai_results_dict = load_csv_to_dict(ai_results)
    except Exception as e:
        print(f"Error: {e}")
        ai_results = get_classified_items("\n".join(unclassified_apps.keys()))
        ai_results_dict = load_csv_to_dict(ai_results)

    for app_name, classified_type in ai_results_dict.items():
        if classified_type == "productive" and app_name in unclassified_apps:
            productive_apps[app_name] = unclassified_apps[app_name]
        elif classified_type == "unproductive" and app_name in unclassified_apps:
            unproductive_apps[app_name] = unclassified_apps[app_name]

    try:
        return get_analysis(productive_apps, unproductive_apps)
    except Exception as e:
        print(f"Error: {e}")
        return get_analysis(productive_apps, unproductive_apps)

def generate_year_report():
    """
    Placeholder function for generating a yearly report.

    This function is currently not implemented.
    """
    pass