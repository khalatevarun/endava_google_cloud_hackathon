# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""social_media_agent: for social media strategy and content planning"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash-001"

social_media_agent = Agent(
    model=MODEL,
    name="social_media_agent",
    instruction=prompt.SOCIAL_MEDIA_AGENT_PROMPT,
    output_key="social_media_output",
    tools=[],  # Add sub-tools/agents here as needed
)
