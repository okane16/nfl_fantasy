# Here is a sample aggregation query that calculates the number of daily active users
# based on the number of unique users who complete a sign-in activity each day.

from moose_lib import (
    AggregationCreateOptions,
    AggregationDropOptions,
    Blocks,
    ClickHouseEngines,
    TableCreateOptions,
    create_aggregation,
    drop_aggregation,
)

destination_table = "DailyActiveUsers"
materialized_view = "DailyActiveUsers_mv"

select_sql = """
SELECT 
    toStartOfDay(timestamp) as date,
    uniqState(userId) as dailyActiveUsers
FROM ParsedActivity_0_0
WHERE activity = 'Login' 
GROUP BY toStartOfDay(timestamp)
"""

teardown_queries = drop_aggregation(
    AggregationDropOptions(materialized_view, destination_table)
)

table_options = TableCreateOptions(
    name=destination_table,
    columns={"date": "Date", "dailyActiveUsers": "AggregateFunction(uniq, String)"},
    engine=ClickHouseEngines.MergeTree,
    order_by="date",
)

aggregation_options = AggregationCreateOptions(
    table_create_options=table_options,
    materialized_view_name=materialized_view,
    select=select_sql,
)

setup_queries = create_aggregation(aggregation_options)

block = Blocks(teardown=teardown_queries, setup=setup_queries)
