# Function Call Mapping Graph

```mermaid
graph TD
    subgraph code_vector_index_py[code/vector_index.py]
        code_vector_index_py__l2_normalize[_l2_normalize]
        code_vector_index_py___init__[__init__]
        code_vector_index_py__load[_load]
        code_vector_index_py_persist[persist]
        code_vector_index_py_clear[clear]
        code_vector_index_py_add[add]
        code_vector_index_py_search[search]
        code_vector_index_py_size[size]
        code_vector_index_py_dim[dim]
    end
    subgraph code_gateway_py[code/gateway.py]
        code_gateway_py__is_up[_is_up]
        code_gateway_py_ensure_gateway[ensure_gateway]
        code_gateway_py_embed[embed]
    end
    subgraph code_persistence_py[code/persistence.py]
        code_persistence_py__atomic_write[_atomic_write]
        code_persistence_py_list_sessions[list_sessions]
        code_persistence_py___init__[__init__]
        code_persistence_py_query_path[query_path]
        code_persistence_py_graph_path[graph_path]
        code_persistence_py__legacy_graph_path[_legacy_graph_path]
        code_persistence_py_write_query[write_query]
        code_persistence_py_read_query[read_query]
        code_persistence_py_write_graph[write_graph]
        code_persistence_py_read_graph[read_graph]
        code_persistence_py__node_path[_node_path]
        code_persistence_py_write_node[write_node]
        code_persistence_py_read_node[read_node]
        code_persistence_py_read_all_nodes[read_all_nodes]
    end
    subgraph code_recovery_py[code/recovery.py]
        code_recovery_py_classify_failure[classify_failure]
        code_recovery_py_plan_recovery[plan_recovery]
        code_recovery_py_handle_critic_verdict[handle_critic_verdict]
    end
    subgraph code_skills_py[code/skills.py]
        code_skills_py_resolve_inputs[resolve_inputs]
        code_skills_py__format_memory_hits[_format_memory_hits]
        code_skills_py_render_prompt[render_prompt]
        code_skills_py_parse_skill_json[parse_skill_json]
        code_skills_py_tool_payload[tool_payload]
        code_skills_py_run_skill[run_skill]
        code_skills_py___init__[__init__]
        code_skills_py_prompt_template[prompt_template]
        code_skills_py_get[get]
        code_skills_py_names[names]
    end
    subgraph code_memory_py[code/memory.py]
        code_memory_py__load[_load]
        code_memory_py__save[_save]
        code_memory_py__index[_index]
        code_memory_py__try_embed[_try_embed]
        code_memory_py__tokens[_tokens]
        code_memory_py__keyword_search[_keyword_search]
        code_memory_py__vector_search[_vector_search]
        code_memory_py_read[read]
        code_memory_py__persist_item[_persist_item]
        code_memory_py__fallback_remember[_fallback_remember]
        code_memory_py_remember[remember]
        code_memory_py__llm_classify[_llm_classify]
        code_memory_py_record_outcome[record_outcome]
        code_memory_py_add_fact[add_fact]
        code_memory_py_clear[clear]
    end
    subgraph code_flow_py[code/flow.py]
        code_flow_py_main[main]
        code_flow_py___init__[__init__]
        code_flow_py_add_node[add_node]
        code_flow_py_mark[mark]
        code_flow_py_ready_nodes[ready_nodes]
        code_flow_py_has_running[has_running]
        code_flow_py_extend_from[extend_from]
        code_flow_py_run[run]
        code_flow_py__run_one[_run_one]
    end
    subgraph code_decision_py[code/decision.py]
        code_decision_py__format_hits[_format_hits]
        code_decision_py__format_history[_format_history]
        code_decision_py__format_attached[_format_attached]
        code_decision_py_next_step[next_step]
    end
    subgraph code_action_py[code/action.py]
        code_action_py__result_to_text[_result_to_text]
        code_action_py_execute[execute]
    end
    subgraph code_sandbox_py[code/sandbox.py]
        code_sandbox_py__truncate[_truncate]
        code_sandbox_py_run_python[run_python]
    end
    subgraph code_replay_py[code/replay.py]
        code_replay_py__print_block[_print_block]
        code_replay_py__expand_prompt[_expand_prompt]
        code_replay_py__expand_output[_expand_output]
        code_replay_py_replay[replay]
        code_replay_py_main[main]
    end
    subgraph code_schemas_py[code/schemas.py]
        code_schemas_py_new_id[new_id]
        code_schemas_py_all_done[all_done]
        code_schemas_py_next_unfinished[next_unfinished]
        code_schemas_py_is_answer[is_answer]
    end
    subgraph code_artifacts_py[code/artifacts.py]
        code_artifacts_py_put[put]
        code_artifacts_py_get_bytes[get_bytes]
        code_artifacts_py_get_meta[get_meta]
        code_artifacts_py_exists[exists]
    end
    subgraph code_perception_py[code/perception.py]
        code_perception_py__snapshot_history[_snapshot_history]
        code_perception_py__snapshot_hits[_snapshot_hits]
        code_perception_py_observe[observe]
    end
    subgraph code_mcp_runner_py[code/mcp_runner.py]
        code_mcp_runner_py__dispatch_tool[_dispatch_tool]
        code_mcp_runner_py_run_with_tools[run_with_tools]
        code_mcp_runner_py__chat[_chat]
    end
    subgraph code_mcp_server_py[code/mcp_server.py]
        code_mcp_server_py__safe[_safe]
        code_mcp_server_py__empty_usage[_empty_usage]
        code_mcp_server_py__load_usage[_load_usage]
        code_mcp_server_py__save_usage[_save_usage]
        code_mcp_server_py__bump[_bump]
        code_mcp_server_py__under_cap[_under_cap]
        code_mcp_server_py__tavily_search[_tavily_search]
        code_mcp_server_py__ddg_search[_ddg_search]
        code_mcp_server_py__crawl4ai_fetch[_crawl4ai_fetch]
        code_mcp_server_py_web_search[web_search]
        code_mcp_server_py_fetch_url[fetch_url]
        code_mcp_server_py_get_time[get_time]
        code_mcp_server_py_currency_convert[currency_convert]
        code_mcp_server_py_read_file[read_file]
        code_mcp_server_py_list_dir[list_dir]
        code_mcp_server_py_create_file[create_file]
        code_mcp_server_py_update_file[update_file]
        code_mcp_server_py_edit_file[edit_file]
        code_mcp_server_py__read_for_index[_read_for_index]
        code_mcp_server_py__chunk_text[_chunk_text]
        code_mcp_server_py_index_document[index_document]
        code_mcp_server_py_search_knowledge[search_knowledge]
    end
    subgraph gateway_db_py[gateway/db.py]
        gateway_db_py_conn[conn]
        gateway_db_py_init[init]
        gateway_db_py_log_call[log_call]
        gateway_db_py_by_agent[by_agent]
        gateway_db_py_recent[recent]
        gateway_db_py_aggregate[aggregate]
    end
    subgraph gateway_client_py[gateway/client.py]
        gateway_client_py_ask[ask]
        gateway_client_py___init__[__init__]
        gateway_client_py_chat[chat]
        gateway_client_py_chat_batch[chat_batch]
        gateway_client_py_capabilities[capabilities]
        gateway_client_py_cost_by_agent[cost_by_agent]
        gateway_client_py_embed[embed]
    end
    subgraph gateway_cache_py[gateway/cache.py]
        gateway_cache_py___init__[__init__]
        gateway_cache_py__key[_key]
        gateway_cache_py_get_or_create[get_or_create]
    end
    subgraph gateway_embedders_py[gateway/embedders.py]
        gateway_embedders_py_build_embedders[build_embedders]
        gateway_embedders_py_embed_with_failover[embed_with_failover]
        gateway_embedders_py___init__[__init__]
        gateway_embedders_py__gc[_gc]
        gateway_embedders_py_can_use[can_use]
        gateway_embedders_py_record[record]
        gateway_embedders_py_mark_failure[mark_failure]
        gateway_embedders_py_snapshot[snapshot]
        gateway_embedders_py_embed[embed]
    end
    subgraph gateway_providers_py[gateway/providers.py]
        gateway_providers_py__flatten_system[_flatten_system]
        gateway_providers_py__empty_result[_empty_result]
        gateway_providers_py__model_supports_reasoning[_model_supports_reasoning]
        gateway_providers_py__gemini_supports_thinking[_gemini_supports_thinking]
        gateway_providers_py__gemini_thinking_knob[_gemini_thinking_knob]
        gateway_providers_py__gemini_inline_refs[_gemini_inline_refs]
        gateway_providers_py__gemini_clean_schema[_gemini_clean_schema]
        gateway_providers_py__coerce_obj[_coerce_obj]
        gateway_providers_py__ollama_native_tools[_ollama_native_tools]
        gateway_providers_py__prompted_tool_system[_prompted_tool_system]
        gateway_providers_py__parse_prompted_tool_call[_parse_prompted_tool_call]
        gateway_providers_py_model_capabilities[model_capabilities]
        gateway_providers_py_build_providers[build_providers]
        gateway_providers_py_build_router_providers[build_router_providers]
        gateway_providers_py___init__[__init__]
        gateway_providers_py_chat[chat]
        gateway_providers_py_stream[stream]
        gateway_providers_py__headers[_headers]
        gateway_providers_py__translate_tools[_translate_tools]
        gateway_providers_py__translate_messages[_translate_messages]
        gateway_providers_py__apply_response_format[_apply_response_format]
        gateway_providers_py__apply_reasoning[_apply_reasoning]
        gateway_providers_py_walk[walk]
        gateway_providers_py_strip[strip]
    end
    subgraph gateway_router_py[gateway/router.py]
        gateway_router_py_resolve[resolve]
        gateway_router_py___init__[__init__]
        gateway_router_py__day_start[_day_start]
        gateway_router_py_gc[gc]
        gateway_router_py_can_use[can_use]
        gateway_router_py_record[record]
        gateway_router_py_mark_unavailable[mark_unavailable]
        gateway_router_py_snapshot[snapshot]
        gateway_router_py_candidates[candidates]
        gateway_router_py_pick[pick]
        gateway_router_py_all_status[all_status]
    end
    subgraph gateway_main_py[gateway/main.py]
        gateway_main_py__estimate_tokens[_estimate_tokens]
        gateway_main_py__build_sample[_build_sample]
        gateway_main_py__tier_from_count[_tier_from_count]
        gateway_main_py__parse_tier[_parse_tier]
        gateway_main_py__classify_tier[_classify_tier]
        gateway_main_py_lifespan[lifespan]
        gateway_main_py__normalize_messages[_normalize_messages]
        gateway_main_py__system_blocks[_system_blocks]
        gateway_main_py__est_tokens[_est_tokens]
        gateway_main_py__backoff_for[_backoff_for]
        gateway_main_py__required_caps[_required_caps]
        gateway_main_py__validate_structured[_validate_structured]
        gateway_main_py_chat[chat]
        gateway_main_py_chat_batch[chat_batch]
        gateway_main_py_cost_by_agent[cost_by_agent]
        gateway_main_py_embed[embed]
        gateway_main_py_list_embedders[list_embedders]
        gateway_main_py_list_providers[list_providers]
        gateway_main_py_capabilities[capabilities]
        gateway_main_py_status[status]
        gateway_main_py_routers[routers]
        gateway_main_py_calls[calls]
        gateway_main_py_index[index]
        gateway_main_py_help_page[help_page]
        gateway_main_py__one[_one]
        gateway_main_py_gen[gen]
    end
    %% Example edges (truncated for brevity) 
    code_vector_index_py___init__ --> code_memory_py__load
    code_vector_index_py___init__ --> code_vector_index_py__load
    code_vector_index_py__load --> code_artifacts_py_exists
    code_vector_index_py_clear --> code_artifacts_py_exists
    code_vector_index_py_add --> code_vector_index_py__l2_normalize
    code_gateway_py_embed --> gateway_embedders_py_embed
    code_gateway_py_embed --> gateway_main_py_embed
    code_gateway_py_embed --> gateway_client_py_embed
    code_persistence_py_write_graph --> code_flow_py_add_node
    code_persistence_py_read_graph --> code_skills_py_get
    code_recovery_py_plan_recovery --> code_recovery_py_classify_failure
    code_skills_py_run_skill --> code_sandbox_py_run_python
    code_skills_py_run_skill --> code_skills_py_parse_skill_json
    code_memory_py__index --> code_vector_index_py_add
    code_flow_py_main --> code_flow_py_run
    code_flow_py__run_one --> code_skills_py_run_skill
    code_decision_py_next_step --> gateway_main_py_chat
    code_action_py_execute --> code_artifacts_py_put
    code_sandbox_py_run_python --> code_sandbox_py__truncate
    code_replay_py_replay --> code_replay_py__expand_output
    code_mcp_server_py_web_search --> code_mcp_server_py__tavily_search
    gateway_client_py_ask --> gateway_main_py_chat
    gateway_main_py_chat --> gateway_providers_py_chat
    gateway_main_py_chat --> gateway_client_py_chat
    gateway_providers_py_chat --> gateway_providers_py__ollama_native_tools
    gateway_providers_py_chat --> gateway_providers_py__parse_prompted_tool_call
    gateway_providers_py_chat --> gateway_providers_py_strip
    gateway_router_py_resolve --> code_skills_py_get
```mermaid
