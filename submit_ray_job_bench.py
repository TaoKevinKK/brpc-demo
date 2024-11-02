import time
from datetime import datetime
from typing import List, Dict

# 假设 JobSubmissionClient、JobStatus 和相关函数已从 Ray 的相关模块导入
from ray.job_submission import JobSubmissionClient, JobStatus

# 如果有自定义的 wait_until_status 函数，请确保导入或定义它
# from your_module import wait_until_status

def submit_and_monitor_multiple_jobs(ray_url: str, entrypoint: str, num_jobs: int = 100, wait_seconds: int = 60) -> List[Dict[str, str]]:
    """
    提交多个 Ray 作业，并在等待指定时间后查询每个作业的状态。

    Args:
        ray_url (str): Ray 集群的 URL。
        entrypoint (str): 作业的入口点命令。
        num_jobs (int, optional): 要提交的作业数量。默认值为 100。
        wait_seconds (int, optional): 等待查询作业状态的秒数。默认值为 60。

    Returns:
        List[Dict[str, str]]: 包含每个作业的 job_id 和提交时间的列表。
    """
    client = JobSubmissionClient(ray_url)
    submitted_jobs = []

    print(f"开始提交 {num_jobs} 个作业...")

    for i in range(1, num_jobs + 1):
        try:
            job_id = client.submit_job(
                entrypoint=entrypoint,
                runtime_env={"working_dir": "./"}
            )
            submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            submitted_jobs.append({'job_id': job_id, 'submission_time': submission_time})
            print(f"提交作业 {i}/{num_jobs}，Job ID: {job_id}，提交时间: {submission_time}")
        except Exception as e:
            print(f"提交作业 {i}/{num_jobs} 失败，错误: {e}")//:

    print(f"所有作业已提交。等待 {wait_seconds} 秒后开始查询作业状态...")
    time.sleep(wait_seconds)

    print("开始查询作业状态...")
    for job in submitted_jobs:
        job_id = job['job_id']
        try:
            status = client.get_job_status(job_id)
            print(f"作业 ID: {job_id}，提交时间: {job['submission_time']}，状态: {status}")
        except Exception as e:
            print(f"查询作业 ID: {job_id} 状态失败，错误: {e}")

    return submitted_jobs

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="提交多个 Ray 作业并监控状态")
    parser.add_argument("--ray-url", type=str, required=True, help="Ray 集群的 URL，例如 ray://127.0.0.1:10001")
    parser.add_argument("--entrypoint", type=str, required=True, help="作业的入口点命令，例如 'python my_job.py'")
    parser.add_argument("--num-jobs", type=int, default=100, help="要提交的作业数量，默认值为 100")
    parser.add_argument("--wait-seconds", type=int, default=60, help="等待查询作业状态的秒数，默认值为 60 秒")

    args = parser.parse_args()

    submit_and_monitor_multiple_jobs(
        ray_url=args.ray_url,
        entrypoint=args.entrypoint,
        num_jobs=args.num_jobs,
        wait_seconds=args.wait_seconds
    )