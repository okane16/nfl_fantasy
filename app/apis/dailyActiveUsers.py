from moose_lib import MooseClient

def run(client: MooseClient, params):
    minDailyActiveUsers = int(params.get('minDailyActiveUsers', [0])[0])
    limit = int(params.get('limit', [10])[0])

    return client.query(
        '''SELECT
            date,
            uniqMerge(dailyActiveUsers) as dailyActiveUsers
        FROM DailyActiveUsers
        GROUP BY date
        HAVING dailyActiveUsers >= {minDailyActiveUsers}
        ORDER BY date
        LIMIT {limit}''',
        {
            "minDailyActiveUsers": minDailyActiveUsers,
            "limit": limit
        }
    )
