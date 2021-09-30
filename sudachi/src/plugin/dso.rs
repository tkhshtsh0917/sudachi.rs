/*
 *  Copyright (c) 2021 Works Applications Co., Ltd.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

/// Create an entry point into sudachi DSO plugin
#[macro_export]
macro_rules! sudachi_dso_plugin {
    ($plugin_type:ty, $impl_type:ty) => {
        #[no_mangle]
        pub fn load_plugin() -> SudachiResult<<$plugin_type as PluginCategory>::BoxType> {
            let object = <$impl_type>::default();
            let boxed: <$plugin_type as PluginCategory>::BoxType = Box::new(object);
            Ok(boxed)
        }
    };
}