# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
import json

from perf_insights.results import output_formatter


class JSONOutputFormatter(output_formatter.OutputFormatter):
  def __init__(self, output_file):
    # TODO(nduca): Resolve output_file here vs output_stream in base class.
    super(JSONOutputFormatter, self).__init__(output_file)
    self.output_file = output_file

  def Format(self, results):
    run_dict = dict([(run_info.run_id, run_info.AsDict()) for run_info
                     in results.all_run_infos])
    all_values_list = [v.AsDict() for v in results.all_values]
    full_result = {
      'runs': run_dict,
      'values': all_values_list
    }

    json.dump(full_result, self.output_file, indent=2)
    self.output_file.flush()